import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MandarCitaComponent } from './mandar-cita.component';

describe('MandarCitaComponent', () => {
  let component: MandarCitaComponent;
  let fixture: ComponentFixture<MandarCitaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MandarCitaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MandarCitaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
