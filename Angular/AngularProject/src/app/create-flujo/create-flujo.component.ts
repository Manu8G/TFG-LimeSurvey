import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-create-flujo',
  templateUrl: './create-flujo.component.html',
  styleUrl: './create-flujo.component.css'
})

export class CreateFlujoComponent {
  data: any = {};
  IDSurveyL: any = {};
  modifiedData: any;
  myControl = new FormControl('');
  idSurvey: string[] = ['123456'];
  filteredOptions!: Observable<string[]>;
  preguntas: string[] = [''];

  constructor(private service: CreateSurveyServiceService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    // this.service.listIDSurvey(this.IDSurveyL).subscribe({
    //   next: (response) => {
    //     let keys = Object.keys(response);
    //     let values = Object.values(response);
        
    //     for(let i = 0; i < keys.length; i++){
    //       this.idSurvey.push(keys[i] + " - " + values[i]);
    //     }
    //     this.idSurvey.push('alo');
        
    //     console.log("La idSurvey: ");
    //     console.log(this.idSurvey);
    //     //console.dir(this.idSurvey);
    //     this.cdr.detectChanges();
    //   },
    //   error: (err) => {
    //     console.error('Error:', err);
    //   }
    // });
    
    this.filteredOptions = this.myControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );
    
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    console.log("EL value es: ",value);
    return this.idSurvey.filter(idSurvey => idSurvey.toLowerCase().includes(filterValue));
  }

  addInput(): void {
    this.preguntas.push('');
  }

  onSubmit() {
    this.data.survey_id = this.myControl;
    console.log("El id es: "+this.data.survey_id);
    this.service.createSection(this.data).subscribe({
      next: (response) => {
        //console.log("La estructura de datos en angular es V2: ");
        //console.dir(response);
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

}
