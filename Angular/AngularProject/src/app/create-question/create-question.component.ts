import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { Pregunta } from '../models/pregunta/pregunta.module'
import { PreguntaMultiple } from '../models/pregunta-multiple/pregunta-multiple.module'

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
  idSection: string[] = ['']
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
  
  constructor(private service: CreateSurveyServiceService) {}

  ngOnInit() {
    this.service.listIDSurvey().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.idSurvey.push(keys[i] + " - " + values[i]);
        }
        //console.log("La idSurvey: ");
        //console.dir(this.idSurvey);
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
    
    this.filteredSurveyOptions = this.surveyControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );

    this.idSection = ['Rellena antes la encuesta'];

    this.filteredSectionOptions = this.sectionControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.idSurvey.filter(idSurvey => idSurvey.toLowerCase().includes(filterValue));
  }

  onSubmit() {
    this.data.survey_id = this.surveyControl.value;
    let id_encuesta = this.data.survey_id;
    id_encuesta = id_encuesta.match(/^\d+/);
    this.data.survey_id = id_encuesta[0];

    this.data.id_seccion = this.sectionControl.value;
    let id_seccion = this.data.id_seccion;
    id_seccion = id_seccion.match(/^\d+/);
    this.data.id_seccion = id_seccion[0];
    // this.data.tipo = this.tipo;
    let vare = '';
    for(let i = 0; i < this.tipos.length; i++){
      if(this.tipos[i].value == this.tipo){
        let aux = this.tipos[i].viewValue;
        console.log("aux: ", aux);
        vare = String(aux.charAt(0));
      }
    }
    this.data.tipo = vare;
    
    if(this.data.tipo == 'T'){
      const pregu: Pregunta  = {
        nombre_real: this.data.question_title,
        cuerpo_pregunta: this.cuerpo,
        id_encuesta: this.data.survey_id,
        id_seccion: this.data.id_seccion,
        tipo_pregunta: this.data.tipo
      };
      this.service.createTextQuestion(pregu).subscribe({
        next: (response) => {
          this.modifiedData = response;
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });
    }else{
      const pregu: PreguntaMultiple  = {
        nombre_real: this.data.question_title,
        cuerpo_pregunta: this.cuerpo,
        id_encuesta: this.data.survey_id,
        id_seccion: this.data.id_seccion,
        tipo_pregunta: this.data.tipo,
        respuestas: []
      };
      this.service.createMultipleQuestion(pregu).subscribe({
        next: (response) => {
          this.modifiedData = response;
        },
        error: (err) => {
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

  onFirstSelectChange() {
    this.idSection = [];
    this.data.survey_id = this.surveyControl;
    let id_encuesta = this.data.survey_id.value;
    id_encuesta = id_encuesta.match(/\d+/);
    this.service.listIDSection(id_encuesta[0]).subscribe({
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

}
