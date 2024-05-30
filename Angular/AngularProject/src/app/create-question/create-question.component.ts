import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-create-question',
  templateUrl: './create-question.component.html',
  styleUrl: './create-question.component.css'
})
export class CreateQuestionComponent implements OnInit{
  data: any = {};
  IDSurveyL: any = {};
  IDSectionL: any = {};
  modifiedData: any;
  surveyControl = new FormControl('');
  sectionControl = new FormControl('');
  idSurvey: string[] = ['111111'];
  idSection: string[] = ['222222']
  filteredSurveyOptions!: Observable<string[]>;
  filteredSectionOptions!: Observable<string[]>;
  datosP: any[] = [];
  valueS: string = '';
  datosPArray: [string, any][] = [];
  continue:boolean = true;
  cont:number = 0;
  contAny:any;
  tipos = [
    { value: 'hide', viewValue: 'T - Texto' },
    { value: 'show', viewValue: 'M - Multiple opcion' }
  ];
  tipo:string='';
  showElements: boolean = false;
  preguntas: string[] = [''];
  
  constructor(private service: CreateSurveyServiceService) {}

  ngOnInit() {
    this.service.listIDSurvey(this.IDSurveyL).subscribe({
      next: (response) => {
        /*console.log("La estructura de datos en angular es V2: ");
        console.dir(response);*/
        //console.log("EL tipo es: ",typeof response);
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.valueS = keys[i] + " - " + values[i];
          //console.log("EL valueS es: ",this.valueS);
          this.idSurvey.push(this.valueS);
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

    this.service.listIDSection(this.IDSectionL).subscribe({
      next: (response) => {
        /*console.log("La estructura de datos en angular es V2: ");
        console.dir(response);*/
        //console.log("EL tipo es: ",typeof response);
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.valueS = keys[i] + " - " + values[i];
          //console.log("EL valueS es: ",this.valueS);
          this.idSection.push(this.valueS);
        }
        //console.log("La idSurvey: ");
        //console.dir(this.idSurvey);
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });

    this.filteredSectionOptions = this.sectionControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );
    //console.log("EL filteredOptions es: ",this.filteredOptions);
    
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    //console.log("EL value es: ",value);
    return this.idSurvey.filter(idSurvey => idSurvey.toLowerCase().includes(filterValue));
  }

  onSubmit() {
    this.data.survey_id = this.surveyControl;
    this.service.createQuestion(this.data).subscribe({
      next: (response) => {
        //console.log("La estructura de datos en angular es V2: ");
        //console.dir(response);
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

  checkVisibility(): void {
    this.showElements = this.tipo === 'show';
  }

  addInput(): void {
    this.preguntas.push('');
  }

}
