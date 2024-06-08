import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { Router } from '@angular/router';
import { Usuario } from '../models/usuario/usuario.module';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  title = 'AngularProject';
  
  loginData = {
    name: '',
    password: ''
  };

  data: any = {};
  modifiedData: any;

  constructor(private surveyService: CreateSurveyServiceService, private router: Router) {} //, private cookieService: CookieService

  onSubmit(){
    const usuar: Usuario  = {
      name: this.loginData.name,
      password: this.loginData.password
    };
    const usuarJSON = JSON.stringify(usuar);
    this.surveyService.createToken(usuar).subscribe({
      next: (response) => {
        //console.log("La estructura de datos en angular es V2: ");
        //console.dir(response);
        this.modifiedData = response;
        if(this.modifiedData.hasOwnProperty('access_token')){
          //console.log('TOKEN CORRECTO')
          //this.cookieService.set('access_token', this.modifiedData.access_token);
          this.router.navigateByUrl('/');
          //console.log(this.router.url)
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }
}
