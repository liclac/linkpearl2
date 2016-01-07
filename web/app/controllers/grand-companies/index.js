import Ember from 'ember';
import _ from 'lodash/lodash';

export default Ember.Controller.extend({
  splitByRank: false,
  filterByGC: null,

  tableData: Ember.computed('model.gcs', 'model.stats', 'splitByRank', 'filterByGC', function() {
    let gcs = this.get('model.gcs').reduce((cur, gc) => {
      cur[gc.id] = {
        id: gc.id,
        label: gc.get('name'),
        name: gc.get('name'),
        slug: gc.get('slug'),
        short: gc.get('short'),
        ranks: gc.get('ranks').map((rank) => {
          return {
            rank: rank.get('rank'),
            name: rank.get('name'),
            num_characters: 0,
          };
        }),
        num_characters: 0,
      };
      return cur;
    }, {});

    this.get('model.stats').forEach((stat) => {
      if (stat.gc === null) {
        return;
      }

      gcs[stat.gc].num_characters += stat.num_characters;
      gcs[stat.gc].ranks[stat.gc_rank].num_characters = stat.num_characters;
    });

    let data = _.values(gcs);

    if (this.get('filterByGC')) {
      let filterID = this.get('filterByGC.id');
      data = data.filter((gc) => { return gc.id === filterID; });
    }

    if (this.get('splitByRank')) {
      let newData = [];
      data.forEach((gc) => {
        gc.ranks.forEach((rank) => {
          if (rank.rank == 0) {
            return;
          }

          let d = _.clone(gc);
          d.label += ': ' + rank.rank + '. ' + rank.name;
          d.rank = rank.rank;
          d.rank_name = rank.name;
          d.num_characters = rank.num_characters;
          newData.push(d);
        });
      });
      data = newData;
    }

    return data.map((d) => { return Ember.Object.create(d); });
  }),
  chartData: Ember.computed('tableData', function() {
    return this.get('tableData').map(function(gc) {
      return { label: gc.get('label'), value: gc.get('num_characters') };
    });
  }),
});
