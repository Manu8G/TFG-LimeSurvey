import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service'
import { Id } from '../models/id/id.module';

@Component({
  selector: 'app-modify-survey',
  templateUrl: './modify-survey.component.html',
  styleUrl: './modify-survey.component.css'
})
export class ModifySurveyComponent {
  items: string[] = [];
  idSurvey: string[] = [];

  constructor(private surveyService: CreateSurveyServiceService) {}

  eliminarEncuesta(encuesta: String){
    for (const item of this.idSurvey) {
      // Dividimos cada item por el separador " ' " para separar el identificador y el nombre
      const partes = item.split(" - ");
      // Checamos si el segundo elemento (nombre de la encuesta) coincide con el nombreEncuesta proporcionado
      if (partes[1] === encuesta) {
        console.log('esta es la elegida: ',item);
        console.log('esta es la elegida id: ',partes[0]);
        const idEncuesta: Id  = {
          Id: String(partes[0]) 
        };
        this.surveyService.eliminarEncuesta(idEncuesta);
      }
    }
  }


  ngOnInit(): void {
    this.surveyService.listIDSurvey().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.idSurvey.push(keys[i] + " - " + values[i]);
          this.items.push(String(values[i]));
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });

    // this.items = ['USU1','USU2','USU3','USU4','USU5','USU6','USU7'];

  }

}
