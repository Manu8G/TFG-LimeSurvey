import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FlujoService } from '../services/flujo/flujo.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { ChangeDetectorRef } from '@angular/core';
import { Flujo } from '../models/flujo/flujo.module'

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
  idSurvey: string[] = [''];
  filteredOptions!: Observable<string[]>;
  encuestas: string[] = [''];
  encuestaNameId: Map<string, any> = new Map<string, any>();
  encuestasId: string[] = [];

  constructor(private service: CreateSurveyServiceService, private flujoService: FlujoService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.service.listIDSurvey().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        keys.forEach((key, index) => {
          // console.log('key: ',key);
          // console.log('values: ',values[index]);
          this.encuestaNameId.set(key, values[index]);
        });
        for(let i = 0; i < keys.length; i++){
          this.idSurvey.push(String(values[i]));
        }
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
    
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
    this.encuestas.push('');
  }

  onSubmit() {
    this.data.survey_id = this.myControl;
    
    for (let [key, val] of this.encuestaNameId.entries()) {
      this.encuestas.forEach(encuesta => {
        if (encuesta === val) {
              this.encuestasId.push(key);
            }
      });
    }

    const flujo:  Flujo = {
      id_usuario: this.data.id_usuario,
      tipo_de_flujo: this.data.tipo_de_flujo,
      encuestas: this.encuestasId
    };

    this.flujoService.createFlujo(flujo).subscribe({
      next: (response) => {
        this.modifiedData = response;
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

}
