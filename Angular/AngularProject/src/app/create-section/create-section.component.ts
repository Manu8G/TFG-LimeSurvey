import { Component } from '@angular/core';
import { CreateSectionServiceService } from '../services/create_section/create-section-service.service';

@Component({
  selector: 'app-create-section',
  templateUrl: './create-section.component.html',
  styleUrl: './create-section.component.css'
})
export class CreateSectionComponent {
  data: any = {};
  modifiedData: any;
  variable: any = 3;

  constructor(private sectionService: CreateSectionServiceService) {}

  onSubmit() {
    this.sectionService.modifyData(this.data).subscribe({
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
