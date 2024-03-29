import { Component } from '@angular/core';
import { FillItems } from '@app/classes/researcher-profil';

@Component({
    selector: 'app-researchers-list',
    templateUrl: './researchers-list.component.html',
    styleUrls: ['./researchers-list.component.scss'],
})
export class ResearchersListComponent {
    profiles = FillItems();
}
