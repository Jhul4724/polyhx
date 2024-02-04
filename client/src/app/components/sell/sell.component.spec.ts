import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResearchersListComponent } from './sell.component';

describe('ResearchersListComponent', () => {
  let component: ResearchersListComponent;
  let fixture: ComponentFixture<ResearchersListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ResearchersListComponent]
    });
    fixture = TestBed.createComponent(ResearchersListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
