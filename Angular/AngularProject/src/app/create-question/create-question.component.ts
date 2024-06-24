import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { Pregunta } from '../models/pregunta/pregunta.module'
import { PreguntaMultiple } from '../models/pregunta-multiple/pregunta-multiple.module'
import { Id } from '../models/id/id.module'
import { ActivatedRoute } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-question',
  templateUrl: './create-question.component.html',
  styleUrl: './create-question.component.css'
})
export class CreateQuestionComponent implements OnInit{
  data: any = {};
  modifiedData: any;
  surveyControl = new FormControl('');
  sectionControl = new FormControl('');
  idSurvey: string[] = [''];
  idSection: string[] = [''];
  idEncuesta: string = '';
  filteredSurveyOptions!: Observable<string[]>;
  filteredSectionOptions!: Observable<string[]>;
  tipos = [
    { value: 'hide', viewValue: 'T - Texto' },
    { value: 'show', viewValue: 'M - Multiple opcion' }
  ];
  tipo:string='';
  showElementsM: boolean = false;
  showElementsT: boolean = false;
  respuestas: string[] = [''];
  cuerpo:string='';
  
  constructor(private service: CreateSurveyServiceService, private router: Router, private toastr: ToastrService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.idEncuesta = params['id']; 
    });
    
    const id: Id  = {
      Id: this.idEncuesta
    };

    this.service.listIDSection(id).subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.idSection.push(keys[i] + " - " + values[i]);
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }


  onSubmit() {

    this.data.id_seccion = this.sectionControl.value;
    let id_seccion = this.data.id_seccion; 
    id_seccion = id_seccion.match(/^\d+/);
    this.data.id_seccion = id_seccion[0];
    let vare = '';
    for(let i = 0; i < this.tipos.length; i++){
      if(this.tipos[i].value == this.tipo){
        let aux = this.tipos[i].viewValue;
        vare = String(aux.charAt(0));
      }
    }
    this.data.tipo = vare;
    
    if(this.data.tipo == 'T'){
      const pregu: Pregunta  = {
        nombre_real: this.data.question_title,
        cuerpo_pregunta: this.cuerpo,
        id_encuesta: this.idEncuesta,
        id_seccion: this.data.id_seccion,
        tipo_pregunta: this.data.tipo
      };
      this.service.createTextQuestion(pregu).subscribe({
        next: (response) => {
          this.modifiedData = response;
          let mensaje = this.data.question_title + ' se creo con exito';
          this.toastr.success(mensaje,'Pregunta creada');
          this.router.navigate(['/modify_survey'])
        },
        error: (err) => {
          this.toastr.error('No se pudo crear la pregunta', 'Error');
          console.error('Error:', err);
        }
      });
    }else{
      const pregu: PreguntaMultiple  = {
        nombre_real: this.data.question_title,
        cuerpo_pregunta: this.cuerpo,
        id_encuesta: this.idEncuesta,
        id_seccion: this.data.id_seccion,
        tipo_pregunta: this.data.tipo,
        respuestas: this.respuestas
      };
      
      this.service.createMultipleQuestion(pregu).subscribe({
        next: (response) => {
          this.modifiedData = response;
          let mensaje = this.data.question_title + ' se creo con exito';
          this.toastr.success(mensaje,'Pregunta creada');
          this.router.navigate(['/modify_survey'])
        },
        error: (err) => {
          this.toastr.error('No se pudo crear la pregunta', 'Error');
          console.error('Error:', err);
        }
      });
    }
    
  }

  checkVisibility(): void {
    this.showElementsM = this.tipo === 'show';
  }

  addInput(): void {
    this.respuestas.push('');
  }

}
