import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { Observable } from 'rxjs/internal/Observable';
import { FormControl } from '@angular/forms';
import { Flujo } from '../models/flujo/flujo.module';

@Component({
  selector: 'app-asignar-flujo',
  templateUrl: './asignar-flujo.component.html',
  styleUrl: './asignar-flujo.component.css'
})
export class AsignarFlujoComponent {
  items: string[] = [];
  data: any = {};
  modifiedData: any;
  surveyControl = new FormControl('');
  sectionControl = new FormControl('');
  idSurvey: string[] = [''];
  idSection: string[] = ['']
  filteredSurveyOptions!: Observable<string[]>;
  filteredSectionOptions!: Observable<string[]>;


  constructor(private serviceSurvey: CreateSurveyServiceService, private flujoService: FlujoService) {}

  ngOnInit(): void {
    this.serviceSurvey.listProfesionalUsers().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.items.push(String(values[i]));
        }
        
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });  

    this.flujoService.listFlujos().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.items.push(String(values[i]));
        }
        
      },
      error: (err) => {
        console.error('Error:', err);
      }
    }); 

  }

  onSubmit() {
    const pregu: Flujo  = {
      encuestas: this.data.question_title,
      id_usuario: '',
      tipo_de_flujo: this.data.survey_id
    };
    this.flujoService.asignarFlujo(pregu).subscribe({
      next: (response) => {
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

}
