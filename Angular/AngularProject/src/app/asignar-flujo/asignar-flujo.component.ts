import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { Observable } from 'rxjs/internal/Observable';
import { FormControl } from '@angular/forms';
import { Caso } from '../models/caso/caso.module';
import { UsuarioRole } from '../models/usuario-role/usuario-role.module';
import { FlujoId } from '../models/flujo-id/flujo-id.module';
import { ActivatedRoute } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-asignar-flujo',
  templateUrl: './asignar-flujo.component.html',
  styleUrl: './asignar-flujo.component.css'
})
export class AsignarFlujoComponent {
  usuarios: string[] = [];
  flujos: string[] = [];
  data: any = {};
  modifiedData: any;
  surveyControl = new FormControl('');
  sectionControl = new FormControl('');
  ususe: UsuarioRole[] = [];
  flujoId: FlujoId [] = [];
  idUsuario: String = '';

  constructor(private serviceSurvey: CreateSurveyServiceService, private router: Router, private route: ActivatedRoute, private toastr: ToastrService, private flujoService: FlujoService) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.idUsuario = params['id']; // Access the 'id' parameter from the URL
      console.log('Test ID flujo:', this.idUsuario);
    });
    // this.serviceSurvey.listProfesionalUsers().subscribe({
    //   next: (response) => {
    //     this.ususe = response;
    //     for(let i = 0; i < this.ususe.length; i++){
    //       this.usuarios.push(String(this.ususe[i].nombre));
    //     }
        
    //   },
    //   error: (err) => {
    //     console.error('Error:', err);
    //   }
    // });  

    this.flujoService.listFlujos().subscribe({
      next: (response) => {
        this.flujoId = response;
        for(let i = 0; i < this.flujoId.length; i++){
          this.flujos.push(String(this.flujoId[i].nombre));
        }
        
      },
      error: (err) => {
        console.error('Error:', err);
      }
    }); 

  }

  onSubmit() {
    // console.log("id_flujo: ",String(this.sectionControl.value))
    // console.log("id_usuario: ",String(this.surveyControl.value))
    // let id_usu = '';
    let id_flu = '';
    let name_flu = '';
    // for(let i = 0; i < this.ususe.length; i++){
    //   if(String(this.ususe[i].nombre) == String(this.surveyControl.value)){
    //     id_usu = this.ususe[i].id;
    //   }
    // }
    for(let i = 0; i < this.flujoId.length; i++){
      if(String(this.flujoId[i].nombre) == String(this.sectionControl.value)){
        id_flu = this.flujoId[i].id;
        name_flu = this.flujoId[i].nombre;
      }
    }
    
    
    const caso: Caso  = {
      id_flujo: String(id_flu),
      id_usuario: String(this.idUsuario)
    };
    this.flujoService.asignarFlujo(caso).subscribe({
      next: (response) => {
        this.modifiedData = response;
        let mensaje = name_flu + ' se asigno con exito';
        this.toastr.success(mensaje,'Flujo asignado');
        this.router.navigate(['/modify_user'])
      },
      error: (err) => {
        this.toastr.error('No se pudo asignar el flujo', 'Error');
        console.error('Error:', err);
      }
    });
  }

}
