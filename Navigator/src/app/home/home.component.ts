import { Component, OnInit } from '@angular/core';
import { PlaceFetchService } from '../services/place-fetch.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  textEntered: string = '';

  constructor(private plyFetch: PlaceFetchService) {}

  ngOnInit(): void {
    // document.body.className = 'selector';
  }
  onSearch() {
    console.log('inside search');
    // this.plyFetch.toSearch = this.textEntered;
    // this.viewPackage.viewPlacePackages = this.textEntered;
  }
  ngOnDestroy() {
    // document.body.className = '';
  }
}
