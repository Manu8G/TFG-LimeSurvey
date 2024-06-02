import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateFlujoComponent } from './create-flujo.component';

describe('CreateFlujoComponent', () => {
  let component: CreateFlujoComponent;
  let fixture: ComponentFixture<CreateFlujoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CreateFlujoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CreateFlujoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
