import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VendrePageComponent } from './vendre-page.component';

describe('VendrePageComponent', () => {
  let component: VendrePageComponent;
  let fixture: ComponentFixture<VendrePageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VendrePageComponent]
    });
    fixture = TestBed.createComponent(VendrePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
