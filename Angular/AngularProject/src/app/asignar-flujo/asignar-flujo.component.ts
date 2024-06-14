import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { Observable } from 'rxjs/internal/Observable';
import { FormControl } from '@angular/forms';
import { Caso } from '../models/caso/caso.module';
import { UsuarioRole } from '../models/usuario-role/usuario-role.module';
import { FlujoId } from '../models/flujo-id/flujo-id.module';

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

  constructor(private serviceSurvey: CreateSurveyServiceService, private flujoService: FlujoService) {}

  ngOnInit(): void {
    this.serviceSurvey.listProfesionalUsers().subscribe({
      next: (response) => {
        this.ususe = response;
        for(let i = 0; i < this.ususe.length; i++){
          this.usuarios.push(String(this.ususe[i].nombre));
        }
        
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });  

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
    let id_usu = '';
    let id_flu = '';
    for(let i = 0; i < this.ususe.length; i++){
      if(String(this.ususe[i].nombre) == String(this.surveyControl.value)){
        id_usu = this.ususe[i].id;
      }
    }
    for(let i = 0; i < this.flujoId.length; i++){
      if(String(this.flujoId[i].nombre) == String(this.sectionControl.value)){
        id_flu = this.flujoId[i].id;
      }
    }
    
    
    const caso: Caso  = {
      id_flujo: String(id_flu),
      id_usuario: String(id_usu)
    };
    this.flujoService.asignarFlujo(caso).subscribe({
      next: (response) => {
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

}
