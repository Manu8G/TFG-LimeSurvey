import { ActivatedRouteSnapshot, CanActivate, GuardResult, MaybeAsync, Router, RouterStateSnapshot } from '@angular/router'
import { AuthenticationService } from '../services/authentication/authentication.service'
import { Injectable } from '@angular/core'

@Injectable({
    providedIn: 'root',
})

export class AuthGuard implements CanActivate {
    constructor(private router: Router, private authenticationService: AuthenticationService){} //private authenticationService: AuthenticationService

    canActivate(): boolean {
        if(!this.authenticationService.isAuthenticated.value){
            this.router.navigate(['/login_page']);
            return false;
        }
        
        return true;
    }

}