import { Component } from '@angular/core';

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

  onSubmit(){
    //logica de usuario
  }
}
