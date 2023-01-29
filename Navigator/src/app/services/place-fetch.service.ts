import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PlaceFetchService {
  toSearch: string = '';
  constructor(private http: HttpClient) {}

  getPlaces(): Observable<any> {
    console.log(this.toSearch);
    return this.http.get<any>(
      'http://127.0.0.1:5000/attractions/' + String(this.toSearch) + '/1'
    );
  }
}
