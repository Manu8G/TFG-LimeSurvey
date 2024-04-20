import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CreateSurveyComponent } from './create-survey/create-survey.component'
import { CreateSectionComponent } from './create-section/create-section.component'

const routes: Routes = [
  { path: 'create_survey', component: CreateSurveyComponent },
  { path: 'create_section', component: CreateSectionComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
