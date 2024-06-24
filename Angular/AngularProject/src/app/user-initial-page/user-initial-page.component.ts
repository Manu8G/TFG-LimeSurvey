import { Component } from '@angular/core';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { UsuarioService } from '../services/usuario/usuario.service';
import { Id } from '../models/id/id.module';
import { tieneCita } from '../models/tiene-cita/tiene-cita.module';

@Component({
  selector: 'app-user-initial-page',
  templateUrl: './user-initial-page.component.html',
  styleUrl: './user-initial-page.component.css'
})
export class UserInitialPageComponent {

  idUsuario: String = '';
  Nombre: String = '';
  Email: String = '';
  DNI: String = '';
  nacionalidad: String = '';
  fechaNacimiento: String = '';
  estado: String = '';
  aviso: String = '';
  tieneCita: boolean = false;
  fechaCita: string = '';
  horaCita: string = '';
  mostrarBotones: boolean = false;

  constructor(private authenticationService: AuthenticationService, private usuarioService: UsuarioService){
    this.idUsuario = String(this.authenticationService.getUserId());
  }

  ngOnInit(){
    const idUsu: Id  = {
      Id: String(this.idUsuario)
    };

    this.usuarioService.getUserInfo(idUsu).subscribe({
      next: (response) => {
        this.Nombre = response.Nombre;
        this.Email = response.Email;
        this.DNI = response.DNI;
        this.nacionalidad = response.Nacionalidad;
        this.fechaNacimiento = response.Fecha_nacimiento;
        this.estado = response.Estado;
      },
      error: (err) => {
        console.error('Erroroso:', err);
      }
    });
    
    
    this.usuarioService.getCita(idUsu).subscribe({
      next: (response) => {
        this.fechaCita = response.fecha;
        this.horaCita = response.hora;
        if(response.asistencia == 'No'){
          this.tieneCita = false;
          this.mostrarBotones = false;
        }else if(response.asistencia == 'Si'){
          this.tieneCita = true;
          this.mostrarBotones = false;
        }else{
          this.tieneCita = true;
          this.mostrarBotones = true;
        }
      },
      error: (err) => {
        console.error('Erroroso:', err);
      }
    });
    
  }

  aceptarCita(){
    this.mostrarBotones = false;
    const tieneCita: tieneCita  = {
      id_paciente: String(this.idUsuario),
      respuesta: '1'
    };
    this.usuarioService.respuestaCita(tieneCita).subscribe({
      next: (response) => {
        
      },
      error: (err) => {
        console.error('Erroroso:', err);
      }
    });
  }

  rechazarCita(){
    this.tieneCita = false;
    const tieneCita: tieneCita  = {
      id_paciente: String(this.idUsuario),
      respuesta: '0'
    };
    this.usuarioService.respuestaCita(tieneCita).subscribe({
      next: (response) => {
        
      },
      error: (err) => {
        console.error('Erroroso:', err);
      }
    });
  }

}
