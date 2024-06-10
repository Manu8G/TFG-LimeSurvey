import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service'

@Component({
  selector: 'app-modify-survey',
  templateUrl: './modify-survey.component.html',
  styleUrl: './modify-survey.component.css'
})
export class ModifySurveyComponent {
  items: string[] = [];
  idSurvey: string[] = [];

  constructor(private surveyService: CreateSurveyServiceService) {}

  ngOnInit(): void {
    this.surveyService.listIDSurvey().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.idSurvey.push(keys[i] + " - " + values[i]);
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });

    this.items = this.idSurvey;
    // this.items = ['USU1','USU2','USU3','USU4','USU5','USU6','USU7'];

  }

}
