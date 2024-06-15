import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { ChangeDetectorRef } from '@angular/core';
import { Seccion } from '../models/seccion/seccion.module';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-create-section',
  templateUrl: './create-section.component.html',
  styleUrl: './create-section.component.css'
})
export class CreateSectionComponent implements OnInit{
  data: any = {};
  IDSurveyL: any = {};
  modifiedData: any;
  myControl = new FormControl('');
  // idSurvey: string[] = [];
  idEncuesta: string[] = [];
  filteredOptions!: Observable<string[]>;
  datosP: any[] = [];
  valueS: string = '';
  cont:number = 0;
  options:any[] = [];

  constructor(private service: CreateSurveyServiceService, private router: Router, private route: ActivatedRoute, private toastr: ToastrService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.idEncuesta = params['id']; // Access the 'id' parameter from the URL
      console.log('Test ID section:', this.idEncuesta);
    });
    // this.service.listIDSurvey().subscribe({
    //   next: (response) => {
    //     let keys = Object.keys(response);
    //     let values = Object.values(response);
        
    //     for(let i = 0; i < keys.length; i++){
    //       this.idSurvey.push(keys[i] + " - " + values[i]);
    //     }
    //     this.cdr.detectChanges();
    //   },
    //   error: (err) => {
    //     console.error('Error:', err);
    //   }
    // });
    
    // this.filteredOptions = this.myControl.valueChanges.pipe(
    //   startWith(''),
    //   map(value => this._filter(value || '')),
    // );
    
  }

  // private _filter(value: string): string[] {
  //   const filterValue = value.toLowerCase();
  //   //console.log("EL value es: ",value);
  //   return this.idSurvey.filter(idSurvey => idSurvey.toLowerCase().includes(filterValue));
  // }

  onSubmit() {
    // this.data.survey_id = this.myControl;
    // let id_encuesta = this.data.survey_id.value;
    // id_encuesta = id_encuesta.match(/\d+/);
    const seccion: Seccion  = {
      nombre_seccion: this.data.nombre_seccion,
      id_encuesta: String(this.idEncuesta)
    };
    this.service.createSection(seccion).subscribe({
      next: (response) => {
        this.modifiedData = response;
        let mensaje = this.data.nombre_seccion + ' se creo con exito'
        this.toastr.success(mensaje,'Sección creada');
        this.router.navigate(['/modify_survey'])
      },
      error: (err) => {
        this.toastr.error('No se pudo crear la sección', 'Error');
        console.error('Erroroso:', err);
      }
    });
  }
}
