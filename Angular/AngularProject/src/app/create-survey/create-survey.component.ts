import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { Encuesta } from '../models/encuesta/encuesta.module';
import { EncuestaDB } from '../models/encuesta-bd/encuesta-bd.module';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { forkJoin } from 'rxjs';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-survey',
  templateUrl: './create-survey.component.html',
  styleUrl: './create-survey.component.css'
})
export class CreateSurveyComponent {
  data: any = {};
  modifiedData: any;
  idUsuario: number = 0;

  constructor(private surveyService: CreateSurveyServiceService, private router: Router, private toastr: ToastrService, private authenticationService: AuthenticationService) {
    
  }

  onSubmit() {
    const encuesta: Encuesta  = {
      nombre_encuesta: this.data.nombre_encuesta,
      idioma: this.data.idioma
    };
    const encuestadb: EncuestaDB  = {
      nombre: this.data.nombre_encuesta,
      id_usuario: String(this.authenticationService.getUserId())
    };
    forkJoin([this.surveyService.createSurvey(encuesta),this.surveyService.createSurveyInDB(encuestadb)]).subscribe({
      next: (response) => {
            this.modifiedData = response[0];
            let mensaje = this.data.nombre_encuesta + ' se creo con exito'
            this.toastr.success(mensaje,'Encuesta creada');
            this.router.navigate(['/modify_survey'])
          },
          error: (err) => {
            this.toastr.error('No se pudo crear la encuesta', 'Error');
            console.error('Error:', err);
          }
    })


  }
}
