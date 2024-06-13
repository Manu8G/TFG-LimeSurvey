import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service'

@Component({
  selector: 'app-modify-flujo',
  templateUrl: './modify-flujo.component.html',
  styleUrl: './modify-flujo.component.css'
})
export class ModifyFlujoComponent {
  items: string[] = [];

  constructor(private surveyService: CreateSurveyServiceService) {}

  ngOnInit(): void {
    //this.items = ['USU1','USU2','USU3','USU4','USU5','USU6','USU7'];
    this.surveyService.listFlujo().subscribe({
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

  deleteItem(): void {
      // Refresh the list
  }

  updateItem(): void {
    
    
  }
}
