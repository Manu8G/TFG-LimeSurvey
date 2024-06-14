import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { Id } from '../models/id/id.module';

@Component({
  selector: 'app-caso-usuario',
  templateUrl: './caso-usuario.component.html',
  styleUrl: './caso-usuario.component.css'
})
export class CasoUsuarioComponent {
  idUsuario: number = 0;

  constructor(private surveyService: CreateSurveyServiceService, private flujoService: FlujoService, private authenticationService: AuthenticationService) {}

  onSubmit() {
    this.authenticationService.idUsuario$.subscribe(id => {
      // console.log("valladolid: ",id);
      this.idUsuario = Number(id);
    });

    const id: Id  = {
      // Id: String(this.idUsuario)
      Id: '26'
    };

    this.flujoService.getCaso(id).subscribe({
      next: (response) => {
        
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });

    // api.activate_survey(777423)
    // api.add_participant_table(777423)
    // participantes = [{'email': 'manuelmesias@correo.ugr.es', 'lastname': 'Guerrero', 'firstname': 'Manu' }]
    // api.add_participant(777423, participantes)
    // participantesL = api.list_participants(777423)
    // participante = [participant['tid'] for participant in participantesL]
    // print('ID del participante: ' + str(participante[0]))
    // tokensP = [participante[0]]
    // api.invite_participant(777423, tokensP)
    
    
    
  }
}
