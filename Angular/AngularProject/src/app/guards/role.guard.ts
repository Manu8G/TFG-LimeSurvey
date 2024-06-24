import { Injectable } from '@angular/core'
import { ActivatedRouteSnapshot, CanActivate, GuardResult, MaybeAsync, Router, RouterStateSnapshot} from '@angular/router'
import { AuthenticationService } from '../services/authentication/authentication.service'

@Injectable({
    providedIn: 'root',
})

export class RoleGuard implements CanActivate {

    constructor(private authenticationService: AuthenticationService, private router: Router){}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
        const requiredRoles = route.data?.['requiredRoles'] || [];
        if(requiredRoles && this.authenticationService.hasRole(requiredRoles)){
            return true;
        }else{
            this.router.navigate(['/user_initial_page']); 
            return false;
        }
    }

}
