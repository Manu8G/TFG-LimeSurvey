import { Component } from '@angular/core';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { UsuarioService } from '../services/usuario/usuario.service';
import { Id } from '../models/id/id.module';

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

  constructor(private authenticationService: AuthenticationService, private usuarioService: UsuarioService){
    this.idUsuario = String(this.authenticationService.getUserId());
  }

  ngOnInit(){
    const idUsu: Id  = {
      Id: String(this.idUsuario)
    };

    this.usuarioService.getUserInfo(idUsu).subscribe({
      next: (response) => {
        //this.modifiedData = response;
        this.Nombre = response.Nombre;
        this.Email = response.Email;
        this.DNI = response.DNI;
        this.nacionalidad = response.Nacionalidad;
        this.fechaNacimiento = response.Fecha_nacimiento;
        this.estado = response.Estado;
        // this.aviso = response.;
        console.log("esto recibimos: ",response);
      },
      error: (err) => {
        console.error('Erroroso:', err);
      }
    });
  }



}
