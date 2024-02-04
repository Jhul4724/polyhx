import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PlayAreaComponent } from '@app/components/play-area/play-area.component';
import { SidebarComponent } from '@app/components/sidebar/sidebar.component';
import { AppRoutingModule } from '@app/modules/app-routing.module';
import { AppMaterialModule } from '@app/modules/material.module';
import { AppComponent } from '@app/pages/app/app.component';
import { GamePageComponent } from '@app/pages/game-page/game-page.component';
import { MainPageComponent } from '@app/pages/main-page/main-page.component';
import { MaterialPageComponent } from '@app/pages/material-page/material-page.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ResearchersListComponent } from './components/researchers-list/researchers-list.component';
import { SearchBarComponent } from './components/search-bar/search-bar.component';
import { AddModifyPageComponent } from './pages/add-modify-page/add-modify-page.component';
import { AnalyticsPageComponent } from './pages/analytics-page/analytics-page.component';
import { SearchPageComponent } from './pages/search-page/search-page.component';
import { HomeComponent } from './home/home.component';
import { SellComponent } from './sell/sell.component';
import { InscrireComponent } from './inscrire/inscrire.component';
import { ConnecterComponent } from './connecter/connecter.component';
import { AccueilComponent } from './accueil/accueil.component';
import { VendreComponent } from './vendre/vendre.component';
import { VendrePageComponent } from './vendre-page/vendre-page.component';

/**
 * Main module that is used in main.ts.
 * All automatically generated components will appear in this module.
 * Please do not move this module in the module folder.
 * Otherwise Angular Cli will not know in which module to put new component
 */
@NgModule({
    declarations: [
        AppComponent,
        GamePageComponent,
        MainPageComponent,
        MaterialPageComponent,
        PlayAreaComponent,
        SidebarComponent,
        NavbarComponent,
        SearchPageComponent,
        ResearchersListComponent,
        AddModifyPageComponent,
        AnalyticsPageComponent,
        HomeComponent,
        SellComponent,
        InscrireComponent,
        ConnecterComponent,
        AccueilComponent,
        VendreComponent,
        VendrePageComponent,
    ],
    imports: [AppMaterialModule, AppRoutingModule, BrowserAnimationsModule, BrowserModule, FormsModule, HttpClientModule, SearchBarComponent],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
