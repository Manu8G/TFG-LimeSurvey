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
import { InitialPageComponent } from './initial-page/initial-page.component';


@NgModule({
  declarations: [
    AppComponent,
    CreateSurveyComponent,
    CreateSectionComponent,
    CreateQuestionComponent,
    InitialPageComponent,
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
    MatCardModule
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }