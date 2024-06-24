import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service'
import { Id } from '../models/id/id.module';
import { Router } from '@angular/router';

@Component({
  selector: 'app-modify-survey',
  templateUrl: './modify-survey.component.html',
  styleUrl: './modify-survey.component.css'
})
export class ModifySurveyComponent {
  items: any[] = [];
  idSurvey: string[] = [];

  constructor(private surveyService: CreateSurveyServiceService, private router: Router) {}

  eliminarEncuesta(encuesta: string){
    const idEncuesta: Id  = {
      Id: encuesta 
    };
    this.surveyService.eliminarEncuesta(idEncuesta).subscribe();
    window.location.reload();
  }

  rutaSeccion(id: string): void{
    this.router.navigate(['create_section',id]);
  }

  rutaPregunta(id: string): void{
    this.router.navigate(['create_question',id]);
  }

  ngOnInit(): void {
    this.surveyService.listIDSurvey().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.idSurvey.push(keys[i] + " - " + values[i]);
          
          this.items.push({"nombre": values[i], "id":keys[i]});
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }
}
