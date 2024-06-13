import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { Encuesta } from '../models/encuesta/encuesta.module';
import { EncuestaDB } from '../models/encuesta-bd/encuesta-bd.module';
import { AuthenticationService } from '../services/authentication/authentication.service';

@Component({
  selector: 'app-create-survey',
  templateUrl: './create-survey.component.html',
  styleUrl: './create-survey.component.css'
})
export class CreateSurveyComponent {
  data: any = {};
  modifiedData: any;
  idUsuario: number = 0;

  constructor(private surveyService: CreateSurveyServiceService, private authenticationService: AuthenticationService) {}

  onSubmit() {
    this.authenticationService.idUsuario$.subscribe(id => {
      console.log("valladolid: ",id);
      this.idUsuario = Number(id);
    });

    const encuesta: Encuesta  = {
      nombre_encuesta: this.data.nombre_encuesta,
      idioma: this.data.idioma
    };
    
    const encuestadb: EncuestaDB  = {
      nombre: this.data.nombre_encuesta,
      id_usuario: this.idUsuario
    };

    this.surveyService.createSurvey(encuesta).subscribe({
      next: (response) => {
        //console.log("La estructura de datos en angular es V2: ");
        //console.dir(response);
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
    this.surveyService.createSurveyInDB(encuestadb).subscribe({
      next: (response) => {
        //console.log("La estructura de datos en angular es V2: ");
        //console.dir(response);
        console.log(response);
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }
}
