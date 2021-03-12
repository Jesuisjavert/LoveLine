<template>
  <!-- <div>
    <div class="category">d</div>
    <div onload="initTmap()">
      <p id="result"></p>
      <select id="selectLevel">
        <option value="0" selected="selected">교통최적+추천</option>
        <option value="1" >교통최적+무료우선</option>
        <option value="2" >교통최적+최소시간</option>
        <option value="3" >교통최적+초보</option>
      </select>
      <button id="btn_select">적용하기</button>
      
      <div id="map_wrap" class="map_wrap">
        <div id="map_div"></div>
      </div>
		</div>
  </div> -->
	<v-container>
		<v-row>
			<v-col cols="10">
				<v-row>
					<p class="pr-3 mt-1">카테고리 :</p>
					<div class="category-box">
						<v-btn @click="addReatuarantMarkers">음식점</v-btn>
						<v-btn>카페</v-btn>
						<v-btn>숙박시설</v-btn>
						<v-btn @click="addTheaterMarkers">영화관</v-btn>
						<v-btn>박물관</v-btn>
						<v-btn>노래방</v-btn>
						<v-btn @click="addArtMarkers">미술관</v-btn>
						<v-btn>PC방</v-btn>
						<v-btn @click="getRP">경로설정</v-btn>
						<v-btn class="" @click="currentMarker"><v-img src="../../assets/images/location.png"></v-img>현위치</v-btn>
					</div>
				</v-row>
				<div class="category"></div>
					<div onload="initTmap()">
					<p id="result"></p>
					<select id="selectLevel">
						<option value="0" selected="selected">교통최적+추천</option>
						<option value="1" >교통최적+무료우선</option>
						<option value="2" >교통최적+최소시간</option>
						<option value="3" >교통최적+도보</option>
					</select>
					<button id="btn_select">적용하기</button>
					
					<div id="map_wrap" class="map_wrap">
						<div id="map_div"></div>
					</div>
				</div>
			</v-col>
			<v-col cols="2">
				선택한 카테고리 주변 리스트
				<ul v-for="selectSpot in selectSpots"> 
					<v-btn class="mt-2">{{ selectSpot }}</v-btn>
				</ul>
			</v-col>
		</v-row>
		<v-col cols="12">
			내가 짠 코스
		</v-col>
	</v-container>
</template>

<script>
import axios from "axios";
import artdata from "./art.json";
import theaterdata from "./theater.json";
import restaurantdata from "./restaurant.json";

export default {
	data() {
		return {
			map: "",
			clickMarkers: [],
			currentMarkers: [],
			artMarkers: [],
			theaterMarkers: [],
			restaurantMarkers: [],
			marker: [],
			selectCategory: "",
			new_polyLine: [],
			new_Click_polyLine: [],
			selectSpots: [
				// {
				// 	name: "용카",
				// },
				// {
				// 	name: "돈페",
				// },
				// {
				// 	name: "동전노래방"
				// },
				// {
				// 	name: "여기"
				// },
				// {
				// 	name: "저기"
				// },
				// {
				// 	name: "이곳"
				// },
				// {
				// 	name: "저곳"
				// },
			],
		}
	},
	// mounted() {
	// 	this.initTmap()
	// 	var map;
		
	// 	var marker_s, marekr_e, waypoint;
	// 	var resultMarkerArr = [];
	// 	//경로그림정보
	// 	var drawInfoArr = [];
	// 	var resultInfoArr = [];
		
	// },
	// methods: {
	// 	initTmap(){
	// 				var resultMarkerArr = [];
					
	// 				// 1. 지도 띄우기
	// 				var map = new Tmapv2.Map("map_div", {
	// 					center: new Tmapv2.LatLng(37.405278291509404, 127.12074279785197),
	// 					width : "100%",
	// 					height : "400px",
	// 					zoom : 14,
	// 					zoomControl : true,
	// 					scrollwheel : true
						
	// 				});
					
	// 				// 2. 시작, 도착 심볼찍기
	// 				// 시작
	// 				var marker_s = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.402688, 127.103259),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_r_m_s.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker_s);
	// 				// 도착
	// 				var marker_e = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.414382, 127.142571),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_r_m_e.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker_e);
					
	// 				// 3. 경유지 심볼 찍기
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.399569, 127.103790),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_1.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.402748, 127.108913),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_2.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.397153, 127.113403),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_3.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.410135, 127.121210),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_4.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.399400, 127.123296),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_5.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.406327, 127.130933),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_6.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				var marker = new Tmapv2.Marker({
	// 					position : new Tmapv2.LatLng(37.413227, 127.127337),
	// 					icon : "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_b_m_7.png",
	// 					iconSize : new Tmapv2.Size(24, 38),
	// 					map:map
	// 				});
	// 				resultMarkerArr.push(marker);
					
	// 				// 4. 경로탐색 API 사용요청
	// 				var routeLayer; 
	// 				$("#btn_select").click(function(){
				
	// 					var searchOption = $("#selectLevel").val();
						
	// 					var headers = {}; 
	// 					headers["appKey"]="l7xx7adfcc4c049947dab12b02d41e5c39f3";
	// 					headers["Content-Type"]="application/json";
						
	// 					var param = JSON.stringify({
	// 						"startName" : "출발지",
	// 						"startX" : "127.103259",
	// 						"startY" : "37.402688",
	// 						"startTime" : "201708081103",
	// 						"endName" : "도착지",
	// 						"endX" : "127.142571",
	// 						"endY" : "37.414382",
	// 						"viaPoints" : 
	// 							[
	// 							{
	// 								"viaPointId" : "test01",
	// 								"viaPointName" : "name01",
	// 								"viaX" : "127.103790" ,
	// 								"viaY" : "37.399569" 
	// 							},
	// 							{
	// 								"viaPointId" : "test02",
	// 								"viaPointName" : "name02",
	// 								"viaX" : "127.108913" ,
	// 								"viaY" : "37.402748" 
	// 							},
	// 							{
	// 								"viaPointId" : "test03",
	// 								"viaPointName" : "name03",
	// 								"viaX" : "127.113403" ,
	// 								"viaY" : "37.397153" 
	// 							},
	// 							{
	// 								"viaPointId" : "test04",
	// 								"viaPointName" : "name04",
	// 								"viaX" : "127.121210" ,
	// 								"viaY" : "37.410135" 
	// 							},
	// 							{
	// 								"viaPointId" : "test05",
	// 								"viaPointName" : "name05",
	// 								"viaX" : "127.123296" ,
	// 								"viaY" : "37.399400" 
	// 							},
	// 							{
	// 								"viaPointId" : "test06",
	// 								"viaPointName" : "name06",
	// 								"viaX" : "127.130933" ,
	// 								"viaY" : "37.406327" 
	// 							},
	// 							{
	// 								"viaPointId" : "test07",
	// 								"viaPointName" : "name07",
	// 								"viaX" : "127.127337" ,
	// 								"viaY" : "37.413227" 
	// 							}
	// 							],
	// 						"reqCoordType" : "WGS84GEO",
	// 						"resCoordType" : "EPSG3857",
	// 						"searchOption": searchOption
	// 					});
						
	// 					$.ajax({
	// 							method:"POST",
	// 							url:"https://apis.openapi.sk.com/tmap/routes/routeSequential30?version=1&format=json",//
	// 							headers : headers,
	// 							async:false,
	// 							data:param,
	// 							success:function(response){
				
	// 								var resultData = response.properties;
	// 								var resultFeatures = response.features;
									
	// 								// 결과 출력
	// 								var tDistance = "총 거리 : " + resultData.totalDistance + "km,  ";
	// 								var tTime = "총 시간 : " + resultData.totalTime + "분,  ";
	// 								var tFare = "총 요금 : " + resultData.totalFare + "원";
									
	// 								$("#result").text(tDistance+tTime+tFare);
									
	// 								//기존  라인 초기화
									
	// 								if(resultInfoArr > 0){
	// 									for(var i in resultInfoArr){
	// 										resultInfoArr[i].setMap(null);
	// 									}
	// 									var resultInfoArr=[];
	// 								}
									
	// 								for(var i in resultFeatures) {
	// 									var geometry = resultFeatures[i].geometry;
	// 									var properties = resultFeatures[i].properties;
	// 									var polyline_;
										
	// 									var drawInfoArr = [];
										
	// 									if(geometry.type == "LineString") {
	// 										for(var j in geometry.coordinates){
	// 											// 경로들의 결과값(구간)들을 포인트 객체로 변환 
	// 											var latlng = new Tmapv2.Point(geometry.coordinates[j][0], geometry.coordinates[j][1]);
	// 											// 포인트 객체를 받아 좌표값으로 변환
	// 											var convertPoint = new Tmapv2.Projection.convertEPSG3857ToWGS84GEO(latlng);
	// 											// 포인트객체의 정보로 좌표값 변환 객체로 저장
	// 											var convertChange = new Tmapv2.LatLng(convertPoint._lat, convertPoint._lng);
												
	// 											drawInfoArr.push(convertChange);
	// 										}
				
	// 										var polyline_ = new Tmapv2.Polyline({
	// 											path : drawInfoArr,
	// 											strokeColor : "#FF0000",
	// 											strokeWeight: 6,
	// 											map : map
	// 										});
	// 										resultInfoArr.push(polyline_);
											
	// 									}else{
	// 										var markerImg = "";
	// 										var size = "";			//아이콘 크기 설정합니다.
											
	// 										if(properties.pointType == "S"){	//출발지 마커
	// 											markerImg = "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_r_m_s.png";	
	// 											size = new Tmapv2.Size(24, 38);
	// 										}else if(properties.pointType == "E"){	//도착지 마커
	// 											markerImg = "http://tmapapis.sktelecom.com/upload/tmap/marker/pin_r_m_e.png";
	// 											size = new Tmapv2.Size(24, 38);
	// 										}else{	//각 포인트 마커
	// 											markerImg = "http://topopen.tmap.co.kr/imgs/point.png";
	// 											size = new Tmapv2.Size(8, 8);
	// 										}
											
	// 										// 경로들의 결과값들을 포인트 객체로 변환 
	// 										var latlon = new Tmapv2.Point(geometry.coordinates[0], geometry.coordinates[1]);
	// 										// 포인트 객체를 받아 좌표값으로 다시 변환
	// 										var convertPoint = new Tmapv2.Projection.convertEPSG3857ToWGS84GEO(latlon);
											
	// 										var marker_p = new Tmapv2.Marker({
	// 											position: new Tmapv2.LatLng(convertPoint._lat, convertPoint._lng),
	// 											icon : markerImg,
	// 											iconSize : size,
	// 											map:map
	// 										});
											
	// 										resultMarkerArr.push(marker_p);
	// 									}
	// 								}
	// 							},
	// 							error:function(request,status,error){
	// 								console.log("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
	// 							}
	// 						});
	// 				});
	// 			},
				
	// 			addComma(num) {
	// 				var regexp = /\B(?=(\d{3})+(?!\d))/g;
	// 				return num.toString().replace(regexp, ',');
	// 	}
		
	// },
	methods: {
		// map 생성
		// Tmapv2.Map을 이용하여, 지도가 들어갈 div, 넓이, 높이를 설정합니다.
		initTmap() {
		this.map = new window.Tmapv2.Map("map_div", {
			center: new window.Tmapv2.LatLng(35.1409667, 126.9278321), // 지도 초기 좌표
			width: "100%", // map의 width 설정
			height: "57vh", // map의 height 설정
			zoom: 16,
		});
		},
		currentMarker() {
		// HTML5의 geolocation으로 사용할 수 있는지 확인합니다
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition((position) => {
			var lat = position.coords.latitude;
			var lon = position.coords.longitude;
			this.removeCurrentMarker();
			//팝업 생성
			var content =
				"<div style='position: relative; border-bottom: 1px solid #dcdcdc; line-height: 18px; padding: 0 35px 2px 0;'>" +
				"<div style='font-size: 12px; line-height: 15px;'>" +
				"<span style='display: inline-block; width: 14px; height: 14px; background-image: url(/resources/images/common/icon_blet.png); vertical-align: middle; margin: 2px;'></span>현재위치" +
				"</div>" +
				"</div>";

			var currentMarker = new window.Tmapv2.Marker({
				position: new window.Tmapv2.LatLng(lat, lon),
				map: this.map,
			});
			this.currentMarkers.push(currentMarker);
			var InfoWindow = new window.Tmapv2.InfoWindow({
				position: new window.Tmapv2.LatLng(lat, lon),
				content: content,
				type: 2,
				map: this.map,
			});
			this.map.setCenter(new window.Tmapv2.LatLng(lat, lon));
			this.map.setZoom(16);
			});
		}
		// this.map.addListener("click", this.addClickMarker);
		// 지도 객체 생성 후 마커를 등록하는 함수를 수행합니다.
		},
		removeCurrentMarker() {
		for (var i = 0; i < this.currentMarkers.length; i++) {
			this.currentMarkers[i].setMap(null);
		}
		this.currentMarkers = [];
		},

		//미술관
		addArtMarkers() {
		if (this.artMarkers.length != 0) {
			this.removeArtMarkers();
		} else {
			this.selectSpots = []

			for (var i = 0; i < artdata.length; i++) {
			var lat = artdata[i].latitude;
			var lng = artdata[i].longitude;
			var artMarker = new window.Tmapv2.Marker({
				position: new window.Tmapv2.LatLng(lat, lng), //Marker의 중심좌표 설정.
				label: "미술관",
			});
			artMarker.setMap(this.map);
			this.artMarkers.push(artMarker);
			this.map.setCenter(new window.Tmapv2.LatLng(lat, lng));
			this.map.setZoom(14);

			this.selectSpots.push(artdata[i].name);
			}
		}
		},
		removeArtMarkers() {
		for (var i = 0; i < this.artMarkers.length; i++) {
			this.artMarkers[i].setMap(null);
		}
		this.artMarkers = [];
		},

		// 영화관
		addTheaterMarkers() {
		if (this.theaterMarkers.length != 0) {
			this.removeTheaterMarkers();
		} else {
			this.selectSpots = []

			for (var i = 0; i < theaterdata.length; i++) {
			var lat = theaterdata[i].latitude;
			var lng = theaterdata[i].longitude;
			// var theatername = theaterdata[i].name;
			var theaterMarker = new window.Tmapv2.Marker({
				position: new window.Tmapv2.LatLng(lat, lng), //Marker의 중심좌표 설정.
				label: "영화관",
			});
			theaterMarker.setMap(this.map);
			this.theaterMarkers.push(theaterMarker);
			this.map.setCenter(new window.Tmapv2.LatLng(lat, lng));
			this.map.setZoom(14);
			
			this.selectSpots.push(theaterdata[i].name);
			}
		}
		},
		removeTheaterMarkers() {
		for (var i = 0; i < this.theaterMarkers.length; i++) {
			this.theaterMarkers[i].setMap(null);
		}
		this.theaterMarkers = [];
		},

		//음식점
		addReatuarantMarkers() {
		if (this.restaurantMarkers.length != 0) {
			this.removeRestaurantMarkers();
		} else {
			this.selectSpots = []

			for (var i = 0; i < restaurantdata.length; i++) {
			var lat = restaurantdata[i].latitude;
			var lng = restaurantdata[i].longitude;
			var restaurantMarker = new window.Tmapv2.Marker({
				position: new window.Tmapv2.LatLng(lat, lng), //Marker의 중심좌표 설정.
				label: "음식점",
			});
			restaurantMarker.setMap(this.map);
			this.restaurantMarkers.push(restaurantMarker);
			this.map.setCenter(new window.Tmapv2.LatLng(lat, lng));
			this.map.setZoom(14);

			this.selectSpots.push(restaurantdata[i].name);
			}
		}
		},
		removeRestaurantMarkers() {
		for (var i = 0; i < this.restaurantMarkers.length; i++) {
			this.restaurantMarkers[i].setMap(null);
		}
		this.restaurantMarkers = [];
		},
		//경로안내 요청 함수
		getRP() {
			var s_latlng = new window.Tmapv2.LatLng(35.190315, 126.820147);
		var e_latlng = new window.Tmapv2.LatLng(35.190048, 126.824286);
		var optionObj = {
			reqCoordType: "WGS84GEO", //요청 좌표계 옵셥 설정입니다.
			resCoordType: "WGS84GEO", //응답 좌표계 옵셥 설정입니다.
			trafficInfo: "Y",
		};
		var params = {
			onComplete: this.onComplete,
			onProgress: this.onProgress,
			onError: this.onError,
		};

		// TData 객체 생성
		var tData = new window.Tmapv2.extension.TData();

		// TData 객체의 경로요청 함수
		tData.getRoutePlanJson(s_latlng, e_latlng, optionObj, params);
		},

		//경로안내
		onComplete(res) {
			console.log(res._responseData); //json으로 데이터를 받은 정보들을 콘솔창에서 확인할 수 있습니다.

		var jsonObject = new window.Tmapv2.extension.GeoJSON();
		var jsonForm = jsonObject.rpTrafficRead(res._responseData);

		//교통정보 표출시 생성되는 LineColor 입니다.
		var trafficColors = {
			// 사용자가 임의로 색상을 설정할 수 있습니다.
			// 교통정보 옵션 - 라인색상
			trafficDefaultColor: "#f06292", //교통 정보가 없을 때
			trafficType1Color: "#f06292", //원할
			trafficType2Color: "#f06292", //서행
			trafficType3Color: "#f06292", //정체
			trafficType4Color: "#f06292", //정체
		};
		jsonObject.drawRouteByTraffic(this.map, jsonForm, trafficColors);
		this.map.setCenter(new window.Tmapv2.LatLng(35.190582, 126.823012));
		this.map.setZoom(16);
		},

		//데이터 로드중 실행하는 함수입니다.
		onProgress() {},

		//데이터 로드 중 에러가 발생시 실행하는 함수입니다.
		onError() {
			alert("onError");
		},
	},

	mounted() {
		this.initTmap();
	},
}
</script>