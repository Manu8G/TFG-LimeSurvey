import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminInitialPageComponent } from './admin-initial-page.component';

describe('AdminInitialPageComponent', () => {
  let component: AdminInitialPageComponent;
  let fixture: ComponentFixture<AdminInitialPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AdminInitialPageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminInitialPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
