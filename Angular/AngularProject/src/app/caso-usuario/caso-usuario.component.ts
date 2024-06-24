import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { UsuarioService } from '../services/usuario/usuario.service';
import { Id } from '../models/id/id.module';
import { Correo } from '../models/correo/correo.module';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-caso-usuario',
  templateUrl: './caso-usuario.component.html',
  styleUrl: './caso-usuario.component.css'
})
export class CasoUsuarioComponent implements OnInit{
  idUsuario: number = 0;
  tipo_flujo: string = '';
  id_formulario: string[]  = [];
  nombre_encuesta: string[] = [];
  numero_orden: number[] = [];
  nivel_actual: number = 0;
  arrayRelacionEncuestas: any[] = [];


  constructor(private usuarioService: UsuarioService, private router: Router, private route: ActivatedRoute, private flujoService: FlujoService, private authenticationService: AuthenticationService) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.idUsuario = params['id']; // ID del usuario del caso
    });

    const id: Id  = {
      // Id: String(this.idUsuario)
      Id: String(this.idUsuario)
    };

    this.flujoService.getCaso(id).subscribe({
      next: (response) => {
        this.tipo_flujo = response[0].tipo_de_flujo;
        this.nivel_actual = response[0].nivel_actual;

        for(let i=0; i<response.length; i++){
          this.nombre_encuesta.push(response[i].nombre_orden)
          this.numero_orden.push(response[i].numero_orden)
          this.id_formulario.push(response[i].id_formulario)
          this.arrayRelacionEncuestas.push({id: response[i].numero_orden, titulo: response[i].nombre_encuesta})
        }

      },
      error: (err) => {
        console.error('Error:', err);
      }
    }); 
  }


  mandarCorreo(){
    let nivel = this.nivel_actual-1
    const correo: Correo  = {
      id_encuesta: String(this.id_formulario[nivel]),
      id_usuario: String(this.idUsuario)
    };
    this.usuarioService.mandarCorreo(correo).subscribe();
  }

  citaUsuario(){
    this.router.navigate(['cita_usuario',this.idUsuario]);
  }

}
