

$( document ).ready(function() {

    var tablist = [ 'boardDetails', 'attributeDetails', 'weightSettings' ];

    var currentTab = 0;

    var tabs = {
        boardDetails: $('div.tab[tabname="board-details"]'),
        attributeDetails: $('div.tab[tabname="attribute-details"]'),
        weightSettings: $('div.tab[tabname="weight-settings"]')
    };

    nextTab();

    function nextTab() {
        Object.keys(tabs)
            .forEach(function (val) {
                if (val !== tablist[currentTab]) {
                    tabs[val].css('display', 'none');
                } else {
                    tabs[val].css('display', 'block')
                }
            });
    }

    $('li.tab-nav').click(function (e) {
        e.preventDefault();

        currentTab = parseInt($(this).attr('tabnumber'), 10);

        nextTab();

        $('li.tab-nav span').removeClass('active');
        $('li.tab-nav[tabnumber="'+ currentTab +'"] span').toggleClass('active');
    });

    $('button#prevBtn').click(function (e) {
        e.preventDefault();
        currentTab = (currentTab - 1) % 3;
        nextTab();

        $('li.tab-nav span').removeClass('active');
        $('li.tab-nav[tabnumber="'+ currentTab +'"] span').toggleClass('active');
    });

    $('button#nextBtn').click(function (e) {
        e.preventDefault();
        currentTab = (currentTab + 1) % 3;
        nextTab();

        $('li.tab-nav span').removeClass('active');
        $('li.tab-nav[tabnumber="'+ currentTab +'"] span').toggleClass('active');
    });

});