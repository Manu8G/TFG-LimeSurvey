import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { Usuario } from '../models/usuario/usuario.module';
import { Paciente } from '../models/paciente/paciente.module';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrl: './create-user.component.css'
})
export class CreateUserComponent {
  data: any = {};
  modifiedData: any;
  showPacienteFields = false;
  myControl = new FormControl('');
  tipos: string[] = ['admin','profesional','paciente'];

  constructor(private surveyService: CreateSurveyServiceService) {}

  onTipoUsuarioChange(): void {
    this.showPacienteFields = String(this.myControl.value) == 'paciente';
  }

  onSubmit(): void {
    if(String(this.myControl.value) == 'paciente'){
      const usuario: Paciente  = {
        name: this.data.name,
        password: this.data.password,
        role: this.data.role,
        dni: this.data.dni,
        estado: this.data.estado,
        nacionalidad: this.data.nacionalidad,
        fecha_nacimiento: this.data.fecha_nacimiento,
        email: this.data.email,
      };
      
      this.surveyService.createPatientUser(usuario).subscribe({
        next: (response) => {
          //console.log("La estructura de datos en angular es V2: ");
          //console.dir(response);
          this.modifiedData = response;
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });

    }else{
      const usuario: Usuario  = {
        name: this.data.name,
        password: this.data.password,
        role: this.data.role,
        accessToken: '',
      };
      
      this.surveyService.createUser(usuario).subscribe({
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
}
