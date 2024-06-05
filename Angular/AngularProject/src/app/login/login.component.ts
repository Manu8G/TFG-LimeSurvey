import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { Usuario } from '../models/usuario/usuario.module';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  title = 'AngularProject';
  
  loginData = {
    username: '',
    password: ''
  };

  data: any = {};
  modifiedData: any;

  constructor(private surveyService: CreateSurveyServiceService) {}

  onSubmit(){
    const usuar: Usuario  = {
      name: this.loginData.username,
      password: this.loginData.password
    };
    
    this.surveyService.createUser(usuar).subscribe({
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
}
