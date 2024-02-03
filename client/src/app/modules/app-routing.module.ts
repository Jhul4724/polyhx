import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddModifyPageComponent } from '@app/pages/add-modify-page/add-modify-page.component';
import { AnalyticsPageComponent } from '@app/pages/analytics-page/analytics-page.component';
import { MainPageComponent } from '@app/pages/main-page/main-page.component';
import { SearchPageComponent } from '@app/pages/search-page/search-page.component';

const routes: Routes = [
    { path: '', redirectTo: '/search', pathMatch: 'full' },
    { path: 'login', component: MainPageComponent },
    { path: 'search', component: SearchPageComponent },
    { path: 'add-modify', component: AddModifyPageComponent },
    { path: 'analytics', component: AnalyticsPageComponent },
    { path: '**', redirectTo: '/search' },
];

@NgModule({
    imports: [RouterModule.forRoot(routes, { useHash: true })],
    exports: [RouterModule],
})
export class AppRoutingModule {}
