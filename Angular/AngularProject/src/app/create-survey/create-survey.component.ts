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
    // console.log("usuarioIDID: ",this.authenticationService.getUserId());

  }

  onSubmit() {
    // this.authenticationService.idUsuario$.subscribe(id => {
    //   console.log("valladolid: ",id);
    //   this.idUsuario = Number(id);
    // });

    // console.log("usuarioIDID: ",this.authenticationService.getUserId());

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
            //console.log("La estructura de datos en angular es V2: ");
            //console.dir(response);
            this.modifiedData = response[0];
            // console.log(response[1]);
            this.toastr.success('Hello world!', 'Toastr fun!');
            this.router.navigate(['/modify_survey'])
          },
          error: (err) => {
            this.toastr.error('Hello world!', 'Toastr fun!');
            // console.error('Error:', err);
          }
    })


  }
}
