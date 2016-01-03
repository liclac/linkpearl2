import DS from 'ember-data';

export default DS.Model.extend({
  lodestone_id: DS.attr('number'),
  // user

  server: DS.belongsTo('server', { async: true }),
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  // title

  // race
  clan: DS.attr('number'),
  gender: DS.attr('number'),

  // gc
  gc_rank: DS.attr('number'),
  // fc

  // jobs
  levels: DS.hasMany('level', { async: true }),
  // minions
  // mounts
});
