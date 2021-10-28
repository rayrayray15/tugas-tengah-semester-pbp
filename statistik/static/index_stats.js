let getChart2DContext = (id) => { return $(id)[0].getContext(`2d`); };
		
const DAILY_ENDP = `https://apicovid19indonesia-v2.vercel.app/api/indonesia/harian`;
const VAX_ENDP = `https://vaksincovid19-api.vercel.app/api/vaksin`;
const PROV_ENDP = `https://indonesia-covid-19.mathdro.id/api/provinsi/`;

const FG_RED = `rgba(255, 0, 0, 0.6)`;
const FG_BLUE = `rgba(0, 0, 255, 0.6)`;
const FG_GREEN = `rgba(0, 255, 0, 0.6)`;
const FG_PURPLE = `rgba(117, 41, 255, 0.6)`;
const FG_YELLOW = `rgba(255, 221, 0, 0.6)`;
const FG_ORANGE = `rgba(255, 127, 0, 0.6)`;

let mainChart = getChart2DContext(`#main-chart`);
let vaxDemographicChart = getChart2DContext(`#vax-demographic-chart`);
let vaxStageChart = getChart2DContext(`#vax-stage-chart`);
let provinceChart = getChart2DContext(`#province-chart`);
let mainChartObjArr = [];
let provinceObj = {};

$.ajax(
{
	type: `GET`,
	url: DAILY_ENDP,
	success: (data) => {
		let mainChartHospArr = [], mainChartDeathArr = [], mainChartPosArr = [], mainChartRecArr = [], mainChartDateArr = [];
		$.each(data, (i, datum) => 
		{
			mainChartObjArr.push(datum);
		});
		mainChartObjArr = mainChartObjArr.slice(-31);
		
		for(let obj of mainChartObjArr)
		{
			mainChartHospArr.push(obj.dirawat);
			mainChartDeathArr.push(obj.meninggal);
			mainChartPosArr.push(obj.positif);
			mainChartRecArr.push(obj.sembuh);
			mainChartDateArr.push((new Date(obj.tanggal.substring(0, obj.tanggal.indexOf(`T`)))).toLocaleDateString(`id-ID`));
		}
		
		let overallCasesChart = new Chart(mainChart,
		{
			type: `line`,
			data: {
				labels: mainChartDateArr,
				datasets: [
				{
					label: `Kasus Positif`,
					data: mainChartPosArr,
					borderColor: FG_BLUE,
					backgroundColor: FG_BLUE,
				},
				{
					label: `Kasus Sembuh`,
					data: mainChartRecArr,
					borderColor: FG_GREEN,
					backgroundColor: FG_GREEN,
				},
				{
					label: `Kematian`,
					data: mainChartDeathArr,
					borderColor: FG_RED,
					backgroundColor: FG_RED,
				},
				{
					label: `Kasus Dirawat`,
					data: mainChartHospArr,
					borderColor: `FG_PURPLE`,
					backgroundColor: `FG_PURPLE`,
				},],
			},
			options: { 
				scales: { y: { beginAtZero: true, } },
				plugins: 
				{
					title: 
					{
						display: true,
						text: `Pertumbuhan Kasus Harian COVID-19 di Indonesia`,
						font: 
						{
							size: 14,
						},
						color: `rgba(0, 0, 0, 0.8)`,
					},
					legend: 
					{
						labels: 
						{
							usePointStyle: true,
						},
					},
				},
			},
		});
	},
});

$.ajax(
{
	type: `GET`,
	url: VAX_ENDP,
	success: (data) => 
	{
		let vaccineDemographicChart = new Chart(vaxDemographicChart,
		{
			type: `bar`,
			data: 
			{
				labels: [`Tenaga Kesehatan`, `Lansia`, `Petugas Publik`],
				datasets: [
				{
					label: `Sasaran Tervaksinasi`,
					data: [data.sasaranvaksinsdmk, data.sasaranvaksinlansia, data.sasaranvaksinpetugaspublik],
					backgroundColor: [FG_RED, FG_YELLOW, FG_BLUE],
				},],
			},
			options: 
			{
				plugins: 
				{
					title: 
					{
						display: true,
						text: `Sasaran Jumlah Vaksinasi COVID-19 di Indonesia Berdasarkan Demografis`,
						font: 
						{
							size: 14,
						},
						color: `rgba(0, 0, 0, 0.8)`,
						padding: 30,
					},
					legend: 
					{
						display: false,
					},
				},
			},
		});
		let vaccineStageChart = new Chart(vaxStageChart,
		{
			type: `bar`,
			data: 
			{
				labels: [`Vaksin Pertama`, `Vaksin Kedua`],
				datasets: [
				{
					label: `Jumlah Tervaksinasi`,
					data: [data.vaksinasi1, data.vaksinasi2],
					backgroundColor: [FG_ORANGE, FG_GREEN],
				},],
			},
			options: 
			{
				plugins: 
				{
					title: 
					{
						display: true,
						text: `Jumlah Vaksinasi COVID-19 di Indonesia Berdasarkan Tahap`,
						font: 
						{
							size: 14,
						},
						color: `rgba(0, 0, 0, 0.8)`,
						padding: 30,
					},
					legend: 
					{
						display: false,
					},
				},
			},
		});
		let i = 0;
		let totalVax = data.vaksinasi1 + data.vaksinasi2;
		increaseCounter = () => 
		{
			setTimeout(() => 
			{
				$(`#vax-counter`).html(i.toLocaleString(`id-ID`));
				i += Math.floor(totalVax / 15);
				if (i < totalVax) {
					increaseCounter();
				} else {
					$(`#vax-counter`).html(totalVax.toLocaleString(`id-ID`));
				}
			}, 100)
		}

		increaseCounter();  
	},
});

$.ajax(
{
	type: `GET`,
	url: PROV_ENDP,
	success: (data) => 
	{
		let provincesArr = [], casesArr = [];
		$.each(data, (i, datum) => 
		{
			for(let obj of datum)
			{
				if(obj.fid != 35) 
				{
					provincesArr.push(obj.provinsi);
					casesArr.push(obj.kasusPosi);
					provinceObj[obj.provinsi] = [obj.kasusPosi, obj.kasusSemb, obj.kasusMeni];
				}
			}
		});
		let provinceCasesChart = new Chart(provinceChart,
		{
			type: `bar`,
			data: 
			{
				labels: provincesArr,
				datasets: [
				{
					label: `Kasus Positif`,
					data: casesArr,
					backgroundColor: FG_BLUE,
				},],
			},
			options: 
			{
				plugins: 
				{
					title: 
					{
						display: true,
						text: `Jumlah Kasus Positif COVID-19 Per Provinsi`,
						font: 
						{
							size: 14,
						},
						color: `rgba(0, 0, 0, 0.8)`,
						padding: 30,
					},
					legend: 
					{
						display: false,
					},
				},
			},
		});
		provincesArr.sort();
		for(prov of provincesArr)
		{
			$(`#prov-select`).append($(`<option>`, 
			{
				value: prov,
				text: prov
			}));
		}
	},
});

$(`#prov-select`).change(() =>
{
	$(`#prov-pos`).html(provinceObj[$(`#prov-select`).val()][0].toLocaleString(`id-ID`));
	$(`#prov-rec`).html(provinceObj[$(`#prov-select`).val()][1].toLocaleString(`id-ID`));
	$(`#prov-ded`).html(provinceObj[$(`#prov-select`).val()][2].toLocaleString(`id-ID`));
});