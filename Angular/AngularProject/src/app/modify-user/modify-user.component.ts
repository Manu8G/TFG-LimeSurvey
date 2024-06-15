import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { AuthenticationService } from '../services/authentication/authentication.service'
import { UsuarioRole } from '../models/usuario-role/usuario-role.module';
import { Router } from '@angular/router';


@Component({
  selector: 'app-modify-user',
  templateUrl: './modify-user.component.html',
  styleUrl: './modify-user.component.css'
})
export class ModifyUserComponent {
  items: string[] = [];
  ususe: UsuarioRole[] = [];
  constructor(private serviceSurvey: CreateSurveyServiceService, private authenService: AuthenticationService, private router: Router) {}

  ngOnInit(): void {
    if(this.authenService.getRole() == 'admin'){
      this.serviceSurvey.listAdminUsers().subscribe({
        next: (response) => {
          this.ususe = response;
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });   
    }else{
      this.serviceSurvey.listProfesionalUsers().subscribe({
        next: (response) => {
          this.ususe = response;
        },
        error: (err) => {
          console.error('Error:', err);
        }
      }); 
    }
  }

  rutaCaso(id: string){
    this.router.navigate(['caso_usuario',id]);
  }

  rutaFlujo(id: string){
    this.router.navigate(['asignar_flujo',id]);
  }

  deleteItem(): void {
      // Refresh the list
  }

  updateItem(): void {
    
    
  }
}
