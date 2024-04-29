import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-create-section',
  templateUrl: './create-section.component.html',
  styleUrl: './create-section.component.css'
})
export class CreateSectionComponent implements OnInit{
  data: any = {};
  IDSurveyL: any = {};
  modifiedData: any;
  myControl = new FormControl('');
  idSurvey: string[] = [];
  filteredOptions!: Observable<string[]>;
  datosP: any[] = [];
  valueS: string = '';
  datosPArray: [string, any][] = [];
  continue:boolean = true;
  cont:number = 0;
  contAny:any;

  constructor(private service: CreateSurveyServiceService) {}

  ngOnInit() {
    this.service.listIDSurvey(this.IDSurveyL).subscribe({
      next: (response) => {
        /*console.log("La estructura de datos en angular es V2: ");
        console.dir(response);*/
        //console.log("EL tipo es: ",typeof response);
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.valueS = keys[i] + " - " + values[i];
          //console.log("EL valueS: ",keys[i]);
          //console.log("EL valueS: ",values[i]);
          console.log("EL valueS es: ",this.valueS);
          this.idSurvey.push(this.valueS);
        }
        console.log("La idSurvey: ");
        console.dir(this.idSurvey);
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
    
    this.filteredOptions = this.myControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value || '')),
    );
    //console.log("EL filteredOptions es: ",this.filteredOptions);
    
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    console.log("EL value es: ",value);
    return this.idSurvey.filter(idSurvey => idSurvey.toLowerCase().includes(filterValue));
  }

  onSubmit() {
    this.data.survey_id = this.myControl;
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
