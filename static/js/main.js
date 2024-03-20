

// 取得主繪製區塊
const myChart = echarts.init(document.getElementById('main'));
// 呼叫後端資料跟繪製
drawEPS();
// 取得後端資料
function drawEPS() {
    $.ajax(
        {
            url: "/current-EPS-data",
            type: "GET",
            dataType: "json",
            success: (result) => {
                $("#eps_high_company").text(result["highest"]["company"]);
                $("#eps_high_value").text(result["highest"]["current_EPS"]);
                // 待補本公司和


                // 繪製對應區塊並給予必要參數
                drawChat(myChart, "當月試算EPS", "本月稅後EPS", result["company"], result["current_EPS"])
            }
        }
    )
}
function drawChat(chart, title, legend, xData, yData) {
    // 指定圖表的配置項目和數據
    let option = {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: [legend]
        },
        xAxis: {
            data: xData
        },
        yAxis: {},
        series: [
            {
                name: legend,
                type: 'bar',
                data: yData
            }
        ]
    };
    // 使用剛指定的配置項目和數據顯示圖表。
    chart.setOption(option);
}