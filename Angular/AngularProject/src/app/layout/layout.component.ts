import { Component } from '@angular/core';
import { AuthenticationService } from '../services/authentication/authentication.service'

@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {

  constructor (private authenticacionService: AuthenticationService){}

  logout(): void{
    this.authenticacionService.logout();
  }

}
