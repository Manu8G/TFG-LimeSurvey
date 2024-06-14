import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { AuthenticationService } from '../services/authentication/authentication.service'
import { UsuarioRole } from '../models/usuario-role/usuario-role.module';

@Component({
  selector: 'app-modify-user',
  templateUrl: './modify-user.component.html',
  styleUrl: './modify-user.component.css'
})
export class ModifyUserComponent {
  items: string[] = [];
  ususe: UsuarioRole[] = [];
  constructor(private serviceSurvey: CreateSurveyServiceService, private authenService: AuthenticationService) {}

  ngOnInit(): void {
    if(this.authenService.getRole() == 'admin'){
      this.serviceSurvey.listAdminUsers().subscribe({
        next: (response) => {
          this.ususe = response;
          for(let i = 0; i < this.ususe.length; i++){
            this.items.push(String(this.ususe[i].nombre));
          }
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });   
    }else{
      this.serviceSurvey.listProfesionalUsers().subscribe({
        next: (response) => {
          this.ususe = response;
          for(let i = 0; i < this.ususe.length; i++){
            this.items.push(String(this.ususe[i].nombre));
          }
        },
        error: (err) => {
          console.error('Error:', err);
        }
      }); 
    }
    

    
    
  }

  deleteItem(): void {
      // Refresh the list
  }

  updateItem(): void {
    
    
  }
}
