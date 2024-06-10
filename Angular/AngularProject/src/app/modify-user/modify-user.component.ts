import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { AuthenticationService } from '../services/authentication/authentication.service'

@Component({
  selector: 'app-modify-user',
  templateUrl: './modify-user.component.html',
  styleUrl: './modify-user.component.css'
})
export class ModifyUserComponent {
  items: string[] = [];

  constructor(private serviceSurvey: CreateSurveyServiceService, private authenService: AuthenticationService) {}

  ngOnInit(): void {
    if(this.authenService.getRole() == 'admin'){
      this.serviceSurvey.listAdminUsers().subscribe({
        next: (response) => {
          let keys = Object.keys(response);
          let values = Object.values(response);
          
          for(let i = 0; i < keys.length; i++){
            this.items.push(String(values[i]));
          }
          
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });   
    }else{
      this.serviceSurvey.listProfesionalUsers().subscribe({
        next: (response) => {
          let keys = Object.keys(response);
          let values = Object.values(response);
          
          for(let i = 0; i < keys.length; i++){
            this.items.push(String(values[i]));
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
