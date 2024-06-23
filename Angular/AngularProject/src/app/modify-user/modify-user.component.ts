import { Component } from '@angular/core';
import { UsuarioService } from '../services/usuario/usuario.service';
import { AuthenticationService } from '../services/authentication/authentication.service'
import { UsuarioRole } from '../models/usuario-role/usuario-role.module';
import { Router } from '@angular/router';
import { Id } from '../models/id/id.module';


@Component({
  selector: 'app-modify-user',
  templateUrl: './modify-user.component.html',
  styleUrl: './modify-user.component.css'
})
export class ModifyUserComponent {
  items: string[] = [];
  ususe: UsuarioRole[] = [];
  roleUser: string = '';
  constructor(private usuarioService: UsuarioService, private authenService: AuthenticationService, private router: Router) {
    this.roleUser = this.authenService.getRole();
  }

  ngOnInit(): void {
    if(this.roleUser == 'admin'){
      this.usuarioService.listAdminUsers().subscribe({
        next: (response) => {
          this.ususe = response;
        },
        error: (err) => {
          console.error('Error:', err);
        }
      });   
    }else{
      this.usuarioService.listProfesionalUsers().subscribe({
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

  borrarUsuario(id: string): void {
    const idUsuario: Id  = {
      Id: String(id)
    };
    this.usuarioService.borrarUsuario(idUsuario).subscribe({
      next: (response) => {
        this.ususe = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
    window.location.reload();
  }

  
}
