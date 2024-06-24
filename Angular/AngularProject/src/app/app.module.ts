import { NgModule } from '@angular/core';
import { BrowserModule} from '@angular/platform-browser';
import { Validators, FormsModule, ReactiveFormsModule, FormGroup } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { AsyncPipe } from '@angular/common';


//Angular materials
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule} from '@angular/material/menu';
import { MatFormFieldModule} from '@angular/material/form-field';
import { MatDividerModule } from '@angular/material/divider';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import {MatSelectModule} from '@angular/material/select';
import { MatCardModule} from '@angular/material/card';

//Componentes
import { AppComponent } from './app.component';
import { CreateSurveyComponent } from './create-survey/create-survey.component';
import { CreateSectionComponent } from './create-section/create-section.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { CreateQuestionComponent } from './create-question/create-question.component';
import { LoginComponent } from './login/login.component';
import { LayoutComponent } from './layout/layout.component';
import { CreateFlujoComponent } from './create-flujo/create-flujo.component';
import { UserInitialPageComponent } from './user-initial-page/user-initial-page.component';
import { CreateUserComponent } from './create-user/create-user.component';
import { ShowUserInfoComponent } from './show-user-info/show-user-info.component';
import { ModifyFlujoComponent } from './modify-flujo/modify-flujo.component';
import { ModifyUserComponent } from './modify-user/modify-user.component';
import { PruebasComponent } from './pruebas/pruebas.component';
import { ModifySurveyComponent } from './modify-survey/modify-survey.component';
import { AdminInitialPageComponent } from './admin-initial-page/admin-initial-page.component';
import { AsignarFlujoComponent } from './asignar-flujo/asignar-flujo.component';
import { CasoUsuarioComponent } from './caso-usuario/caso-usuario.component';
import { ToastrModule } from 'ngx-toastr';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MandarCitaComponent } from './mandar-cita/mandar-cita.component';


@NgModule({
  declarations: [
    AppComponent,
    CreateSurveyComponent,
    CreateSectionComponent,
    CreateQuestionComponent,
    LoginComponent,
    LayoutComponent,
    CreateFlujoComponent,
    UserInitialPageComponent,
    CreateUserComponent,
    ShowUserInfoComponent,
    ModifyFlujoComponent,
    ModifyUserComponent,
    PruebasComponent,
    ModifySurveyComponent,
    AdminInitialPageComponent,
    AsignarFlujoComponent,
    CasoUsuarioComponent,
    MandarCitaComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    AppRoutingModule,
    MatButtonModule,
    MatToolbarModule,
    MatInputModule,
    MatMenuModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    FormsModule,
    MatDividerModule,
    MatAutocompleteModule,
    AsyncPipe,
    MatSelectModule,
    MatCardModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }