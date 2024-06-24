import { Component } from '@angular/core';
import { CreateSurveyServiceService } from '../services/create_survey/create-survey-service.service';
import { FormControl } from '@angular/forms';
import { map, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { OnInit } from '@angular/core';
import { ChangeDetectorRef } from '@angular/core';
import { Seccion } from '../models/seccion/seccion.module';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

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
  idEncuesta: string[] = [];
  filteredOptions!: Observable<string[]>;
  datosP: any[] = [];
  valueS: string = '';
  cont:number = 0;
  options:any[] = [];

  constructor(private service: CreateSurveyServiceService, private router: Router, private route: ActivatedRoute, private toastr: ToastrService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.idEncuesta = params['id']; 
      console.log('Test ID section:', this.idEncuesta);
    });
  }


  onSubmit() {
    const seccion: Seccion  = {
      nombre_seccion: this.data.nombre_seccion,
      id_encuesta: String(this.idEncuesta)
    };
    this.service.createSection(seccion).subscribe({
      next: (response) => {
        this.modifiedData = response;
        let mensaje = this.data.nombre_seccion + ' se creo con exito'
        this.toastr.success(mensaje,'Sección creada');
        this.router.navigate(['/modify_survey'])
      },
      error: (err) => {
        this.toastr.error('No se pudo crear la sección', 'Error');
        console.error('Erroroso:', err);
      }
    });
  }
}
