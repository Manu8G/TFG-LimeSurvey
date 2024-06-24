import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Cita } from '../models/cita/cita.module';
import { UsuarioService } from '../services/usuario/usuario.service';
import { AuthenticationService } from '../services/authentication/authentication.service';

@Component({
  selector: 'app-mandar-cita',
  templateUrl: './mandar-cita.component.html',
  styleUrl: './mandar-cita.component.css'
})
export class MandarCitaComponent {
  data = {
    descripcion: '',
    fecha: '',
    hora: ''
  };

  idUsuario: number = 0;

  constructor(private router: Router, private authenticationService: AuthenticationService, private route: ActivatedRoute, private usuarioService: UsuarioService) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.idUsuario = params['id']; // ID del usuario del caso
    });
  }


  onSubmit(): void {
    console.log('descripcion: ',this.data.descripcion);
    console.log('fecha: ',this.data.fecha);
    console.log('hora: ',this.data.hora);
    const cita: Cita  = {
      descripcion: String(this.data.descripcion),
      fecha: String(this.data.fecha),
      hora: String(this.data.hora),
      id_paciente: String(this.idUsuario),
      id_profesional: String(this.authenticationService.getUserId())
    };

    this.usuarioService.mandarCita(cita).subscribe();

    //this.router.navigate(['caso_usuario',this.idUsuario]);
  }
}
